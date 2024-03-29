import praw
import time
discordUsername = 'gs._'
replaceWith = '(srry no username rn :c)'

reddit = praw.Reddit(
    client_id="ur_client_id",
    client_secret="ur_client_secret",
    user_agent="ur_useragent",
    username='usernamehere',
    password='passwordhere'
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
