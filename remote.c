#include "define.h"

struct sRemote remote;

const uint8_t IRMapKeyTable[D_REMOTE_KEY_MAX]=
{
	
};

const uint16_t IRMapValueTable[D_REMOTE_KEY_MAX]=
{
	0x7122,
	0x7E22,
	0x5422,
	0x4026,
	0x2026,
	0x3E26
};

void RemoteReceive(void)
{        
	remote.timeout = D_REM_TIMEOUT;
	switch(remote.status)
	{
		case D_REMOTE_HEAD_START:		
			remote.status = D_REMOTE_HEAD_END;	
			RemoteEdge(Rising);
		break;

		case D_REMOTE_HEAD_END:	
			if ((remote.RmtLogicWidth<D_REMOTE_HEAD_MIN)||(remote.RmtLogicWidth>D_REMOTE_HEAD_MAX))
			{
				RemoteInitialize();
			}
			else
			{
				remote.status = D_REMOTE_DATA;				  	
				remote.code = 0;
				remote.bitIndex = 0;
			}
		break;
			
		case D_REMOTE_DATA:	
			
			if ((remote.RmtLogicWidth<D_REM_DATA_MIN)||(remote.RmtLogicWidth>D_REM_DATA_MAX))
			{
				RemoteInitialize();
			}
			else
			{ 		
				remote.code <<= 1;
				if(remote.RmtLogicWidth>D_REM_DATA)	
				remote.code |= 1;
				remote.bitIndex++;
				if (remote.bitIndex >= D_REMOTE_BIT_MAX)
				{
					remote.status = D_REMOTE_HEAD_START;						
					remote.bitIndex = 0;	
					SM_put_event_to_buffer(PHYSICAL_EVENT_REMOTE_RECEIVE_PROCESS);
					RemoteEdge(Falling);

				}				
			}			
		break;	
		default:
		break;
	}
}

void MMI_SM_RemoteReceiveProcess(MMI_SM_physical_events_t event)
{
	if(((remote.code&0x00ff)==D_REMOTE_CATEGORY1)||((remote.code&0x00ff)==D_REMOTE_CATEGORY2))
	{
		remote.valid = TRUE;
		remote.noSignalTimer = D_REM_NOSIGNAL_TIME;
		remote.remoteKey = TRUE;				//the flag indicate key is from remote but not keypad.
		remote.keyValue = RemoteDecode(remote.code);
	}
}

void RemoteEdge(uint8_t edge)
{
	if(edge == Rising)
		TMR00 |= _0040_TAU_TIMN_EDGE_RISING;
	else
		TMR00 &= ~_0040_TAU_TIMN_EDGE_RISING;
}

void RemoteInitialize(void)
{
	remote.status=D_REMOTE_HEAD_START;
	RemoteEdge(Falling);
	remote.valid = FALSE;
	remote.bitIndex=0;
	remote.code=0;
	remote.pressx10ms=0;
}

void Remote10msTimer(void)
{
	if(remote.timeout >0)							//prevent the case-- only enter interrupt once,can't catch head code
	{
		remote.timeout--;
		if(remote.timeout ==0)
		{
			RemoteInitialize();
			return;
		}
	}
	if(remote.noSignalTimer>0)
	{
		remote.noSignalTimer--;
		if(remote.noSignalTimer==0)					
		{
			if(remote.remoteKey==TRUE)
			{
				if(remote.pressx10ms > R_KeyHoldTime)
				{
					if((remote.keyValue == PHYSICAL_EVENT_KEY_FORWARD) ||(remote.keyValue == PHYSICAL_EVENT_KEY_BACKWARD))
					{
						SM_put_event_to_buffer(PHYSICAL_EVENT_BT_STOP_FAST_FORWARD_STEP1);
					}
				}
			}
			if ((remote.pressx10ms > R_KeyShortTime)&&(remote.pressx10ms< R_KeyHoldTime))
			{
				if((remote.keyValue  == PHYSICAL_EVENT_KEY_STOP)
					#ifdef D_LONG_KEY_SLEF_DEFINE
					||(remote.keyValue  == PHYSICAL_EVENT_KEY_FORWARD)
					||(remote.keyValue  == PHYSICAL_EVENT_KEY_BACKWARD)
					#endif
					)
				{
					SM_put_event_to_buffer(remote.keyValue);
				}
			}
			RemoteInitialize();
		}
	}
	if(remote.valid == FALSE)						//remote release
		return;
	remote.pressx10ms++;
	if (remote.pressx10ms == R_KeyShortTime)			//Singleshot key
	{
		if((remote.keyValue  != PHYSICAL_EVENT_KEY_STOP)
			#ifdef D_LONG_KEY_SLEF_DEFINE
			&&(remote.keyValue  != PHYSICAL_EVENT_KEY_FORWARD)
			&&(remote.keyValue  != PHYSICAL_EVENT_KEY_BACKWARD)
			#endif
			)
		{
			SM_put_event_to_buffer(remote.keyValue);
		}
	}
	else 	if(remote.pressx10ms== R_KeyContinueStartTime)	//Continue key
	{
		if ((remote.keyValue == PHYSICAL_EVENT_KEY_VOLUP)
			||(remote.keyValue == PHYSICAL_EVENT_KEY_VOLDN)
			||(remote.keyValue == PHYSICAL_EVENT_KEY_TUNEUP)
			||(remote.keyValue == PHYSICAL_EVENT_KEY_TUNEDN))
		{
			SM_put_event_to_buffer(remote.keyValue);
			remote.pressx10ms-= R_KeyContinuTime;					
		}
	}	
	else if (remote.pressx10ms == R_KeyHoldTime)			//Short and Long key 
	{
		switch(remote.keyValue)
		{
			#ifdef D_LONG_KEY_SLEF_DEFINE
			case PHYSICAL_EVENT_KEY_FORWARD:
				remote.keyValue =PHYSICAL_EVENT_LKEY_FORWARD;
				SM_put_event_to_buffer(remote.keyValue);
				break;
			
			case PHYSICAL_EVENT_KEY_BACKWARD:
				remote.keyValue =PHYSICAL_EVENT_LKEY_BACKWARD;
				SM_put_event_to_buffer(remote.keyValue);
				break;
			#endif	
			case PHYSICAL_EVENT_KEY_STOP:
				remote.keyValue =PHYSICAL_EVENT_LKEY_STOP;
				SM_put_event_to_buffer(remote.keyValue);
				break;
			
			default:
				remote.keyValue =PHYSICAL_EVENT_NONE;
				break;
		}
		
	}
	else if (remote.pressx10ms > R_KeyHoldTime)
	{
		remote.pressx10ms = R_KeyHoldTime+1;
	}
}

/****************************************************************************************
*  FUNCTION NAME:   RemoteDecode
*  INPUTS:          None
*  OUTPUTS:         .
*  VALUE RETURNED:  void
*  DESCRIPTION:     .
*  CAUTIONS: 		.
*****************************************************************************************
* MODIFICATION HISTORY:
* Date			Person			Change
* ---------------------------------------------------------------------------------------
* 2014/12/09    Eric       remote creation
****************************************************************************************/
uint8_t RemoteDecode(uint16_t temp)
{
	uint8_t i;	
	for (i=0;i<D_REMOTE_KEY_MAX;i++)
	{
		if (IRMapValueTable[i]==temp)
		{
			return IRMapKeyTable[i];
		}
	}		
	return PHYSICAL_EVENT_NONE;
}

