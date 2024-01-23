import instaloader

L = instaloader.Instaloader()

# Login (optional but can help bypass some rate limits)
L.context.log_in("your_username", "your_password")  # (NOT SAFE! Only for demonstration. Use environment variables or secrets.)

# Fetch recent posts from a profile
profile = instaloader.Profile.from_username(L.context, "target_username")
posts = profile.get_recent_posts()

# Extract data from posts
for post in posts:
    image_url = post.url
    caption = post.caption
    # Further processing