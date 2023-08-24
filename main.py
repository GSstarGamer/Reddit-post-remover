import praw
import time
discordUsername = 'gs._'
replaceWith = '(srry no username rn :c)'

reddit = praw.Reddit(
    client_id="AOOWUSw8I8hwertRSHOfbA",
    client_secret="_ywfaeY-tsvjXnuZhHFRbyZg0Xte6Q",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    username='GS_StarGamer999',
    password='GSattop420'
)

print(f'Editing comments now')


editedComments = 0
start = time.time()
for comment in reddit.user.me().comments.new(limit=None):
    if discordUsername in comment.body:
        editedText = comment.body.replace(discordUsername, replaceWith)
        comment.edit(editedText)
        print(f'[LOG] Edited comment "{comment.body}"')
        editedComments += 1
end = time.time()

print(f'Finised editing {editedComments} comments in {end - start} secs')

print(f'Editing posts now')

editedPosts = 0
start = time.time()
for post in reddit.user.me().submissions.new(limit=None):
    if discordUsername in post.selftext:
        editedText = post.selftext.replace(discordUsername, replaceWith)
        post.edit(editedText)
        print(f'[LOG] Edited post "{post.title}"')

end = time.time()

print(f'Finised editing {editedPosts} posts in {end - start} secs')
