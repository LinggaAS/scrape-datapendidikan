import requests
import bs4

page = requests.get(
    'https://referensi.data.kemdikbud.go.id/index11.php?kode=010101&level=3')

soup = bs4.BeautifulSoup(page.text, 'lxml')

table = soup.find('table', id="example")

headers = [heading.text for heading in table.find_all('th')]

table_rows = [row for row in table.find_all('tr')]

results = [{headers[index]:cell.text for index,
            cell in enumerate(row.find_all('td'))}for row in table_rows]

print(results)
