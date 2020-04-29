from selenium import webdriver
import time
import codecs


url = 'https://twitter.com/SHAQ'

# open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
time.sleep(2)

already_seen = set()  # keeps track of tweets we have already seen.

# write the tweets to a file
fw = codecs.open('tweets.txt', 'w', encoding='utf8')

for i in range(1):

    # find all elements that have the value "tweet" for the data-testid attribute
    tweets = driver.find_elements_by_css_selector('div[data-testid="tweet"]')
    for tweet in tweets:

        if tweet in already_seen:
            continue  # we have seen this tweet before while scrolling down, ignore
        # first time we see this tweet. Mark as seen and process.
        already_seen.add(tweet)

        txt, comments, retweets, likes, date = 'NA', 'NA', 'NA', 'NA', 'NA'

        try:
            txt = tweet.find_element_by_css_selector(
                "div.css-901oao.r-jwli3a.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0").text
            txt = txt.replace('\n', ' ')
            print(txt)
        except:
            print('no text')

        try:
            commentsElement = tweet.find_element_by_css_selector(
                'div[data-testid="reply"]')
            comments = commentsElement.fine_element_by_css_selector(
                'span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text
            print(comments)
        except:
            print('no comments')

        try:
            retweetElement = tweet.find_element_by_css_selector(
                'div[data-testid="retweet"]')
            retweets = retweetElement.find_element_by_css_selector(
                'span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text
            print(retweets)
        except:
            print('no retweets')

        try:
            likesElement = tweet.find_element_by_css_selector(
                'div[data-testid="like"]')
            likes = likesElement.find_element_by_css_selector(
                'span.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0').text
            print(likes)
        except:
            print('no likes')

        try:
            # dateElement = tweet.find_element_by_css_selector(
            #     'div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2')
            # dateElement = tweet.find_element_by_css_selector(
            #     'a.css-4rbku5.css-18t94o4.css-901oao.r-111h2gw.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0')
            # date = dateElement.getAttribute('title').text
            date = tweet.find_element_by_css_selector(
                "a.css-4rbku5.css-18t94o4.css-901oao.r-1re7ezh.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0").text
            print(date)
        except:
            print('no date')

        # only write tweets that have text or retweets (or both).
        if txt != 'NA' or comments != 'NA' or retweets != 'NA' or likes != 'NA':
            fw.write(txt.replace('\n', ' ')+'\t' +
                     str(comments)+'\t' + str(retweets) + '\t' + str(likes) + '\t' + str(date) + '\n')
        print()

        # scroll down twice to load more tweets
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

fw.close()
