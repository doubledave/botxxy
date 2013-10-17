import urllib, json, HTMLParser

def s4Chan(board, search):
  logo = '3::54chan'
  res = []
  p = HTMLParser.HTMLParser()

  catalog = json.load(urllib.urlopen('https://api.4chan.org/%s/catalog.json' % board))

  for i in catalog:
    for j in i['threads']:
      if search.lower() in j.get('sub', '').lower() or search.lower() in j.get('com', '').lower():
        subject = j.get('sub', 'Empty subject')
        post = p.unescape(j.get('com', 'Empty post')).replace('<br>', ' ')

        if len(post) > 300:
          post = post[0:300]
          post = post + '...'

        text = '%s /%s/ %s | %s | %s (R:%s, I:%s)' % (logo, board, subject, post, 'https://4chan.org/%s/res/%s' % (board, j['no']), j['replies'], j['images'])
        res.append(text)
  return res

def getValidBoards():
  boards = []

  l = json.load(urllib.urlopen('https://api.4chan.org/boards.json'))

  for i in l['boards']:
    boards.append(str(i['board']))

  return boards
