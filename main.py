import instaloader
ig = instaloader.Instaloader()

dp = input("Enter the Username: ")
li = input("past the link: ")
ig.download_profile(dp, profile_pic_only=True)


ig.download_post(li,post=True)