/******************************************************************************************
*
*  Copyright (C) 2012 Phoenix (SZ) Co.,Ltd.   All Rights Reserved
*
*  FILE NAME      : remote.h
*
*  PROGRAMMER(S)  : Eric
*                   
*  DATE CREATED   : 2014/12/09
*
*  SYNOPSIS: 
*
*  VALUE RETURNED:  None.
*
*  DESCRIPTION: 
*              
*  CAUTIONS: None.
*             
*  REFERENCES:
******************************************************************************************
*
* MODIFICATION HISTORY:
*
* Date			Person			Change
* --------------------------------------------------------------------------------------- 
* 2014/12/09    Eric       Initial creation
******************************************************************************************
*
* TRACEABILITY:
*
* Requirement ID	Description
* ---------------------------------------------------------------------------------------
*
*****************************************************************************************/

#ifndef _REMOTE_H
#define _REMOTE_H

/***************************************************************************************/
#include "r_cg_macrodriver.h"
#include "SM.h"
/***************************************************************************************/

/*****************    STRUCT DEFINE  *****************************************************/
struct sRemote
{
    uint16_t    RmtLogicWidth;
    uint8_t     remoteKey           	:1;
    uint8_t     valid               	:1;
    uint8_t     status                  :2;
    uint8_t     value;
    uint16_t    code;
    uint16_t    lastCode;
    uint8_t     bitIndex;
    uint8_t     timeout;
    uint8_t     noSignalTimer;
    uint8_t     repeatTimer;
    uint8_t     pressx10ms;
    uint8_t     keyValue;
};
/***************** END OF STRUCT DEFINE *************************************************/

/*****************   DEFINITIONS  ********************************************************/
#define D_LONG_KEY_SLEF_DEFINE


#define Falling                         0
#define Rising                          1

#define functionKey						1		//In order to transform between FM and AM
#define otherKey						0

#define D_REMOTE_KEY_MAX                6
#define D_REMOTE_BIT_MAX                15

#define D_REMOTE_CATEGORY1              0x22
#define D_REMOTE_CATEGORY2              0x26

#define D_REMOTE_HEAD_START             0           
#define D_REMOTE_HEAD_END               1           
#define D_REMOTE_DATA                   2
#if 1   //20MHz
#define D_REMOTE_HEAD_MAX               (240+10)        //2.4/0.01=240
#define D_REMOTE_HEAD_MIN               (240-10)        //2.4/0.01=240
#define D_REM_DATA_MAX                  (180+10)        //1.8/0.01==180
#define D_REM_DATA_MIN                  (120-10)        //1.2/0.01==120
#define D_REM_DATA                      150             //1.5/0.01==150
#else   //12MHz
#define D_REMOTE_HEAD_MAX               (144+10)        //2.4/0.0167=144
#define D_REMOTE_HEAD_MIN               (144-10)        //2.4/0.0167=144
#define D_REM_DATA_MAX                  (107+10)        //1.8/0.0167=107
#define D_REM_DATA_MIN                  (72-10)         //1.2/0.0167=72
#define D_REM_DATA                      90              //1.5/0.0167=90
#if 0   //16MHz
#define D_REMOTE_HEAD_MAX               (192+10)        //2.4/0.0125=192
#define D_REMOTE_HEAD_MIN               (192-10)        //2.4/0.0125=192
#define D_REM_DATA_MAX                  (144+10)        //1.8/0.0125=144
#define D_REM_DATA_MIN                  (96-10)         //1.2/0.0125=96
#define D_REM_DATA                      120             //1.5/0.0125=120
#endif
#endif
#define D_REM_NOSIGNAL_TIME             11
#define D_REM_TIMEOUT                   D_REM_NOSIGNAL_TIME+1

#define R_KeyHoldTime						200	//x10ms
#define R_KeyHoldTime_h					(R_KeyHoldTime/2)	//x10ms
#define R_KeyContinueStartTime			80	//x10ms
#define R_KeyContinuTime					30	//x 10ms
#define R_KeyShortTime					5	//x 10ms

extern void RemoteReceive(void);
extern void MMI_SM_RemoteReceiveProcess(MMI_SM_physical_events_t event);
extern uint8_t RemoteDecode(uint16_t temp);
extern void Remote10msTimer(void);
extern void RemoteInitialize(void);
extern void RemoteEdge(uint8_t edge);

#endif

