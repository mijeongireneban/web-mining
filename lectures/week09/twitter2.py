from selenium import webdriver
import time,codecs


url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
time.sleep(2)

already_seen=set()#keeps track of tweets we have already seen.

#write the tweets to a file
fw=codecs.open('tweets.txt','w',encoding='utf8') 

for i in range(3):

    print(i)
    #find all elements that have the value "tweet" for the data-testid attribute
    tweets=driver.find_elements_by_css_selector('div[data-testid="tweet"]')#
    print(len(tweets))
    for tweet in tweets:

        
        
        if tweet in already_seen:continue#we have seen this tweet before while scrolling down, ignore
        already_seen.add(tweet)#first time we see this tweet. Mark as seen and process.
        
        txt,retweets,date,comments,likes='NA','NA','NA','NA','NA'
        
        
        try:
            date = tweet.find_element_by_css_selector("a.css-4rbku5.css-18t94o4.css-901oao.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0").text
        
            print(date)
        except:
            print("no date")
        
            
        try: 
            txt=tweet.find_element_by_css_selector("div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0").text
            txt=txt.replace('\n', ' ')
            print(txt)
        except: print ('no text')  
        
        
        try:
            commentElement = tweet.find_element_by_css_selector('div[data-testid="reply"]')
            
            comments=commentElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text
            print(comments) 
            
        except:
            print('no comments') 

        try:
        
            #find the div element that havs the value "retweet" for the data-testid attribute
            retweetElement=tweet.find_element_by_css_selector('div[data-testid="retweet"]')
 
            #find the span element that has all the specified values (space separated) in its class attribute
            retweets=retweetElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text  
            print (retweets)                                    
        except:
            print ('no retweets')
            
        try:
            likesElement = tweet.find_element_by_css_selector('div[data-testid="like"]')
            
            likes=likesElement.find_element_by_css_selector('span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text
            print(likes) 
            
        except:
            print('no likes') 
            
        
      
            

        #only write tweets that have text or retweets (or both). 
        if txt!='NA' or retweets!='NA' or date!='NA' or comments!='NA' or likes!='NA':
            fw.write(txt.replace('\n',' ')+'\t'+str(retweets)+'\t'+str(date)+'\t'+str(comments)+'\t'+str(likes)+'\n') 
        print() 
        print()

        
        #scroll down twice to load more tweets
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

fw.close()