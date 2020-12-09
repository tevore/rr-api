import os
from bs4 import BeautifulSoup
"""This script uses BeautifulSoup to parse and collect table data from a given html_doc pattern.
Once this is done, it applies some transformations based on the data and spits it out to a 
cleaner version of a Cypher create script for Neo4j hydration"""

#consider list of html_docs
html_doc = '''


<table id="rr_table" class="wikitable sortable" style="font-size:100%; text-align:left" border="1">
<tbody><tr>
<th>Draw<sup id="cite_ref-RRE&amp;E_22-0" class="reference"><a href="#cite_note-RRE&amp;E-22">&#91;22&#93;</a></sup><sup id="cite_ref-WWERR_23-0" class="reference"><a href="#cite_note-WWERR-23">&#91;23&#93;</a></sup>
</th>
<th>Entrant<sup id="cite_ref-RRE&amp;E_22-1" class="reference"><a href="#cite_note-RRE&amp;E-22">&#91;22&#93;</a></sup><sup id="cite_ref-WWERR_23-1" class="reference"><a href="#cite_note-WWERR-23">&#91;23&#93;</a></sup>
</th>
<th>Order<sup id="cite_ref-RRE&amp;E_22-2" class="reference"><a href="#cite_note-RRE&amp;E-22">&#91;22&#93;</a></sup><sup id="cite_ref-WWERR_23-2" class="reference"><a href="#cite_note-WWERR-23">&#91;23&#93;</a></sup>
</th>
<th>Eliminated by<sup id="cite_ref-RRE&amp;E_22-3" class="reference"><a href="#cite_note-RRE&amp;E-22">&#91;22&#93;</a></sup><sup id="cite_ref-WWERR_23-3" class="reference"><a href="#cite_note-WWERR-23">&#91;23&#93;</a></sup>
</th>
<th>Time<sup id="cite_ref-RRE&amp;E_22-4" class="reference"><a href="#cite_note-RRE&amp;E-22">&#91;22&#93;</a></sup>
</th>
<th>Eliminations
</th></tr>
<tr>
<td><span data-sort-value="01&#160;!">1</span>
</td>
<td><a href="/wiki/Ax_(wrestler)" title="Ax (wrestler)">Ax</a>
</td>
<td><span data-sort-value="04&#160;!">4</span>
</td>
<td>Mr. Perfect
</td>
<td>14:37
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="02&#160;!">2</span>
</td>
<td><a href="/wiki/Smash_(wrestler)" title="Smash (wrestler)">Smash</a>
</td>
<td><span data-sort-value="01&#160;!">1</span>
</td>
<td>André the Giant
</td>
<td>04:54
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="03&#160;!">3</span>
</td>
<td><a href="/wiki/Andr%C3%A9_the_Giant" title="André the Giant">André the Giant</a>
</td>
<td><span data-sort-value="05&#160;!">5</span>
</td>
<td>Himself (Damien and Jake Roberts)^
</td>
<td>14:55
</td>
<td>4
</td></tr>
<tr>
<td><span data-sort-value="04&#160;!">4</span>
</td>
<td><a href="/wiki/Curt_Hennig" title="Curt Hennig">Mr. Perfect</a>
</td>
<td>11
</td>
<td>Hulk Hogan
</td>
<td>27:58
</td>
<td>1
</td></tr>
<tr>
<td><span data-sort-value="05&#160;!">5</span>
</td>
<td><a href="/wiki/Ronnie_Garvin" class="mw-redirect" title="Ronnie Garvin">Ronnie Garvin</a>
</td>
<td><span data-sort-value="02&#160;!">2</span>
</td>
<td>André the Giant
</td>
<td>02:39
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="06&#160;!">6</span>
</td>
<td><a href="/wiki/Greg_Valentine" title="Greg Valentine">Greg Valentine</a>
</td>
<td><span data-sort-value="08&#160;!">8</span>
</td>
<td>Randy Savage
</td>
<td>19:52
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="07&#160;!">7</span>
</td>
<td><a href="/wiki/Jake_Roberts" title="Jake Roberts">Jake Roberts</a>
</td>
<td><span data-sort-value="03&#160;!">3</span>
</td>
<td>André the Giant
</td>
<td>02:08
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="08&#160;!">8</span>
</td>
<td><a href="/wiki/Ron_Bass_(wrestler)" title="Ron Bass (wrestler)">Ron Bass</a>
</td>
<td><span data-sort-value="07&#160;!">7</span>
</td>
<td>Marty Jannetty and Shawn Michaels
</td>
<td>12:36
</td>
<td>0
</td></tr>
<tr>
<td><span data-sort-value="09&#160;!">9</span>
</td>
<td><a href="/wiki/Shawn_Michaels" title="Shawn Michaels">Shawn Michaels</a>
</td>
<td><span data-sort-value="09&#160;!">9</span>
</td>
<td>Arn Anderson and Randy Savage
</td>
<td>14:30
</td>
<td>1
</td></tr>
<tr>
<td>10
</td>
<td><a href="/wiki/Bushwhacker_Butch" class="mw-redirect" title="Bushwhacker Butch">Bushwhacker Butch</a>
</td>
<td>13
</td>
<td>Hulk Hogan and Bad News Brown
</td>
<td>18:13
</td>
<td>1
</td></tr>
<tr>
<td>11
</td>
<td><a href="/wiki/The_Honky_Tonk_Man" title="The Honky Tonk Man">The Honky Tonk Man</a>
</td>
<td><span data-sort-value="06&#160;!">6</span>
</td>
<td>Bushwhacker Butch and Tito Santana
</td>
<td>04:12
</td>
<td>0
</td></tr>
<tr>
<td>12
</td>
<td><a href="/wiki/Tito_Santana" title="Tito Santana">Tito Santana</a>
</td>
<td>12
</td>
<td>Arn Anderson and Randy Savage
</td>
<td>12:47
</td>
<td>1
</td></tr>
<tr>
<td>13
</td>
<td><a href="/wiki/Bad_News_Brown" class="mw-redirect" title="Bad News Brown">Bad News Brown</a>
</td>
<td>19
</td>
<td>Hulk Hogan
</td>
<td>16:24
</td>
<td>1
</td></tr>
<tr>
<td>14
</td>
<td><a href="/wiki/Marty_Jannetty" title="Marty Jannetty">Marty Jannetty</a>
</td>
<td>10
</td>
<td>Tully Blanchard
</td>
<td>07:52
</td>
<td>1
</td></tr>
<tr>
<td>15
</td>
<td><a href="/wiki/Randy_Savage" title="Randy Savage">Randy Savage</a>
</td>
<td>20
</td>
<td rowspan="3">Hulk Hogan
</td>
<td>12:26
</td>
<td>3
</td></tr>
<tr>
<td>16
</td>
<td><a href="/wiki/Arn_Anderson" title="Arn Anderson">Arn Anderson</a>
</td>
<td>16
</td>
<td>10:00
</td>
<td>2
</td></tr>
<tr>
<td>17
</td>
<td><a href="/wiki/Tully_Blanchard" title="Tully Blanchard">Tully Blanchard</a>
</td>
<td>17
</td>
<td>08:02
</td>
<td>1
</td></tr>
<tr>
<td>18
</td>
<td><a href="/wiki/Hulk_Hogan" title="Hulk Hogan">Hulk Hogan</a>
</td>
<td>21
</td>
<td>Akeem and Big Boss Man
</td>
<td>11:31
</td>
<td>10
</td></tr>
<tr>
<td>19
</td>
<td><a href="/wiki/Bushwhacker_Luke" class="mw-redirect" title="Bushwhacker Luke">Bushwhacker Luke</a>
</td>
<td>15
</td>
<td rowspan="4">Hulk Hogan
</td>
<td>03:08
</td>
<td>0
</td></tr>
<tr>
<td>20
</td>
<td><a href="/wiki/Koko_B._Ware" title="Koko B. Ware">Koko B. Ware</a>
</td>
<td>14
</td>
<td>01:08
</td>
<td>0
</td></tr>
<tr>
<td>21
</td>
<td><a href="/wiki/The_Warlord_(wrestler)" title="The Warlord (wrestler)">The Warlord</a>
</td>
<td>18
</td>
<td>00:02
</td>
<td>0
</td></tr>
<tr>
<td>22
</td>
<td><a href="/wiki/Big_Boss_Man_(wrestler)" title="Big Boss Man (wrestler)">Big Boss Man</a>
</td>
<td>22
</td>
<td>04:18
</td>
<td>1
</td></tr>
<tr>
<td>23
</td>
<td><a href="/wiki/One_Man_Gang" title="One Man Gang">Akeem</a>
</td>
<td>28
</td>
<td>Big John Studd
</td>
<td>18:36
</td>
<td>2
</td></tr>
<tr>
<td>24
</td>
<td><a href="/wiki/Brutus_Beefcake" title="Brutus Beefcake">Brutus Beefcake</a>
</td>
<td>24
</td>
<td>Ted DiBiase and The Barbarian
</td>
<td>13:56
</td>
<td>0
</td></tr>
<tr>
<td>25
</td>
<td><a href="/wiki/The_Red_Rooster" class="mw-redirect" title="The Red Rooster">The Red Rooster</a>
</td>
<td>23
</td>
<td>Ted DiBiase
</td>
<td>11:17
</td>
<td>0
</td></tr>
<tr>
<td>26
</td>
<td><a href="/wiki/The_Barbarian_(wrestler)" title="The Barbarian (wrestler)">The Barbarian</a>
</td>
<td>26
</td>
<td>Rick Martel
</td>
<td>12:15
</td>
<td>2
</td></tr>
<tr style="background: gold">
<td>27
</td>
<td><b><a href="/wiki/Big_John_Studd" title="Big John Studd">Big John Studd</a></b>
</td>
<td><span data-sort-value="30&#160;!">-</span>
</td>
<td><b>Winner</b>
</td>
<td>12:21
</td>
<td>2
</td></tr>
<tr>
<td>28
</td>
<td><a href="/wiki/Hercules_(wrestler)" title="Hercules (wrestler)">Hercules</a>
</td>
<td>25
</td>
<td>Ted DiBiase and The Barbarian
</td>
<td>06:11
</td>
<td>0
</td></tr>
<tr>
<td>29
</td>
<td><a href="/wiki/Rick_Martel" title="Rick Martel">Rick Martel</a>
</td>
<td>27
</td>
<td>Akeem
</td>
<td>05:29
</td>
<td>1
</td></tr>
<tr>
<td>30
</td>
<td><a href="/wiki/Ted_DiBiase" title="Ted DiBiase">Ted DiBiase</a>
</td>
<td>29
</td>
<td>Big John Studd
</td>
<td>06:27
</td>
<td>3
</td></tr></tbody></table>

'''

soup = BeautifulSoup(html_doc, 'html.parser')

tables = soup.find_all('table')

print("-- Draw -- | -- Entrant -- | -- Order -- | -- Eliminated By -- | -- Time -- |")

trs = soup.find_all('tr')
count = 0

for tr in trs:

    if count != 0:

        table_data = tr.find_all('td')
        w_draw = table_data[0].span.contents[0].strip() if table_data[0].span is not None else table_data[0].contents[0].strip()
        w_name = table_data[1].a.contents[0].strip()
        w_order = table_data[2].span.contents[0] if table_data[2].span is not None else table_data[2].contents[0]
        same_elims = table_data[3].get('rowspan') if table_data[3].get('rowspan') is not None else "0"
        w_eliminated_by = table_data[3].contents[0].strip() if same_elims != "0" else table_data[3].contents[0].strip()
        #w_eliminated_by = table_data[3].get('rowspan') #if getrowspan, repeat this
        #if there is a rowspan, we need to repeat the initial number for rowspan times and then
        #assume table_data[3] is time in. If not, table_data[4] will be the time in
        w_time_in = table_data[4].contents[0].strip() if same_elims is not None else table_data[3].contents[0].strip()
        #print(w_eliminated_by)
        #print(w_time_in)
        #print(table_data[1].a.contents[0])
        #print(same_elims)

        if w_order != '-':
            w_order = w_order.strip()
        else:
            w_order = "WON"
            w_eliminated_by = "WON"
        #print(type(table_data[2]))

        print(f"-- {w_draw} -- | -- {w_name}"
              + f" -- | -- {w_order} -- | -- {w_eliminated_by} -- | -- {w_time_in} -- |")
    count += 1

#create cypher script here and move on



# op = open("events.csv", "w")
# limit = 15
# start_id = 1
# start_year = 1988
# name_template_1 = "Royal Rumble("
# name_template_2 = ")"
#
# while start_id < limit:
#
#     print(f"Current id: {start_id}")
#
#     if start_id == 1:
#         op.write("id, name, year\n")
#
#     op.write(f"{start_id}, {name_template_1}{start_year}{name_template_2}, {start_year}\n")
#     start_id += 1
#     start_year += 1
#
# op.close()
