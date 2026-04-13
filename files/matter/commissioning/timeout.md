# Commissioning Timeout

##### 11.19.8.1. OpenCommissioningWindow Command
###### CommissioningTimeout Field
This field SHALL specify the time in seconds during which commissioning session establishment is allowed by the Node. This timeout value SHALL follow guidance as specified in the initial Section 5.4.2.3,  “Announcement  Duration”.  The  CommissioningTimeout  applies  only  to  cessation  of  any announcements and to accepting of new commissioning sessions; it does not apply to abortion of connections, i.e., a commissioning session SHOULD NOT abort prematurely upon expiration of this timeout.

#### 5.4.2.3. Announcement Duration
##### 5.4.2.3.1. Commissionable Announcement Duration
In order to minimize unnecessary pollution of the 2.4 GHz and 5 GHz shared wireless spectrum, especially with device discovery, <font color="#dd00dd">a ommissionable device SHALL NOT announce with a rapid inter­val for a duration longer than 15 minutes after announcement commences</font> . This duration was cho­sen to capture the primary case of a user setting up immediately after powering on for a range of devices, including time to download, install and launch applications, transit rooms within a home,etc.
Note  that  devices  MAY  choose  to  announce  for  less  time  in  order  to  conserve  battery  life  or  for other device-specific reasons. Note that an announcement duration that is too short may result in a poor  setup  experience  for  users.  Shorter  announcement  intervals  SHOULD  only  be  employed  to meet otherwise unattainable device functionality/requirements. To help strike a balance between a good setup experience and conserving battery life, <font color="#dd00dd">a device SHALL NOT announce for a duration of less than 3 minutes after announcement commences</font> .
