import instaloader
ig = instaloader.Instaloader()

dp = input("Enter the Username: ")
print("Downloading ...")
ig.download_profile(dp, profile_pic_only=False)
print("Download complited")
