#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:02:30 2018

@author: caiboqin
"""

from lxml import etree 

html='''<tr>
    <td class="posterColumn">
    <span name="rk" data-value="1"></span>
    <span name="ir" data-value="9.216510839765467"></span>
    <span name="us" data-value="7.791552E11"></span>
    <span name="nv" data-value="1868842"></span>
    <span class="123" name="ur" data-value="-1.7834891602345326"></span>
    </td>
    <td class="titleColumn">
      1.
      <a href="/title/tt0111161" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman" >The Shawshank Redemption</a>
        <span class="secondaryInfo">(1994)</span>
    </td>
    <td class="ratingColumn imdbRating">
            <strong title="9.2 based on 1,868,842 user ratings">9.2</strong>
    </td>
    <td class="ratingColumn">
    <div class="seen-widget seen-widget-tt0111161 pending" data-titleid="tt0111161">
        <div class="inline">
            <div class="pending"></div>
            <div class="unseeable">NOT YET RELEASED</div>
            <div class="unseen"> </div>
            <div class="rating"></div>
            <div class="seen">Seen</div>
            <class>123456</class>
        </div>
    </div>
    </td>
    <td class="watchlistColumn">
        <div class="wlb_ribbon" data-tconst="tt0111161" data-recordmetrics="true"></div>
    </td>
</tr>
'''

imdb=etree.HTML(html)
result=imdb.xpath('//div[@class="inline"]/div/text()')