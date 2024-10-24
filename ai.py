import pandas as pd
import requests
import lxml.html
from datetime import datetime
from urllib.parse import urljoin

pd.set_option('display.max_colwidth', 50)
pd.set_option("display.expand_frame_repr", False)

# New URLs related to Artificial Intelligence
ai_research = "https://www.aitrends.com/ai-research/"
ai_news = "https://www.aitrends.com/category/news/"
ai_development = "https://towardsdatascience.com/tagged/artificial-intelligence"
ai_safety = "https://www.technologyreview.com/c/ai-ethics/"
ai_podcast = "https://twimlai.com/twiml-talk/"
ai_community = "https://www.datasciencecentral.com/"

urls = [
    ai_research,
    ai_news,
    ai_development,
    ai_safety,
    ai_podcast,
    ai_community,
]

# Initialize empty dataframes
ai_df = pd.DataFrame()
ai_news_df = pd.DataFrame()
ai_dev_df = pd.DataFrame()
ai_safety_df = pd.DataFrame()
ai_podcast_df = pd.DataFrame()
ai_community_df = pd.DataFrame()

# Converts each link in the list to its own button with different text
def add_htmllink(x):
    htmllink = [f"""<a href={htmllink} target='_blank' style='text-decoration: none;'>
        <button class='visit-button'>Visit Site</button></a>""" for htmllink in x]
    return htmllink

def style_source(y):
    return f"<div class='source-header'>{y}</div>"

# To parse multiple AI sites
for p in urls:
    print(f"Entering site: {p}")
    page = requests.get(p, headers={'User-Agent': 'Mozilla/5.0'})
    if page.status_code != 200:
        print(f"Failed to retrieve {p}: Status code {page.status_code}")
        continue
    
    doc = lxml.html.fromstring(page.content)

    # AI Research
    if p == ai_research:
        titles = doc.xpath('//h2[@class="entry-title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="entry-content"]/p/text()')[:5]
        links = doc.xpath('//h2[@class="entry-title"]/a/@href')[:5]
        ai_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("AI Trends"),
            "Link": " "
        }, index=[0])
        ai_df = pd.concat([ai_row, ai_df]).reset_index(drop=True)
    
    # AI News
    elif p == ai_news:
        titles = doc.xpath('//h2[@class="post-title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="post-excerpt"]/p/text()')[:5]
        links = doc.xpath('//h2[@class="post-title"]/a/@href')[:5]
        ai_news_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_news_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("AI News"),
            "Link": " "
        }, index=[0])
        ai_news_df = pd.concat([ai_news_row, ai_news_df]).reset_index(drop=True)
    
    # AI Development
    elif p == ai_development:
        titles = doc.xpath('//h3[@class="post-title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="post-excerpt"]/p/text()')[:5]
        links = doc.xpath('//h3[@class="post-title"]/a/@href')[:5]
        ai_dev_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_dev_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("Towards Data Science"),
            "Link": " "
        }, index=[0])
        ai_dev_df = pd.concat([ai_dev_row, ai_dev_df]).reset_index(drop=True)
    
    # AI Safety
    elif p == ai_safety:
        titles = doc.xpath('//h2[@class="title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="summary"]/text()')[:5]
        links = doc.xpath('//h2[@class="title"]/a/@href')[:5]
        ai_safety_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_safety_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("AI Safety"),
            "Link": " "
        }, index=[0])
        ai_safety_df = pd.concat([ai_safety_row, ai_safety_df]).reset_index(drop=True)
    
    # AI Podcast
    elif p == ai_podcast:
        titles = doc.xpath('//h2[@class="post-title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="entry-content"]/p/text()')[:5]
        links = doc.xpath('//h2[@class="post-title"]/a/@href')[:5]
        ai_podcast_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_podcast_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("Data Science Podcast"),
            "Link": " "
        }, index=[0])
        ai_podcast_df = pd.concat([ai_podcast_row, ai_podcast_df]).reset_index(drop=True)
    
    # AI Community
    elif p == ai_community:
        titles = doc.xpath('//h2[@class="title"]/a/text()')[:5]
        descriptions = doc.xpath('//div[@class="entry-content"]/p/text()')[:5]
        links = doc.xpath('//h2[@class="title"]/a/@href')[:5]
        ai_community_df = pd.DataFrame({
            "Title": titles,
            "Description": descriptions,
            "Link": add_htmllink(links)
        })
        ai_community_row = pd.DataFrame({
            "Title": " ",
            "Description": style_source("KDNuggets"),
            "Link": " "
        }, index=[0])
        ai_community_df = pd.concat([ai_community_row, ai_community_df]).reset_index(drop=True)

# Combine all DataFrames for a complete view
final_df = pd.concat([ai_df, ai_news_df, ai_dev_df, ai_safety_df, ai_podcast_df, ai_community_df], ignore_index=True)

# Display the final DataFrame
print(final_df)
