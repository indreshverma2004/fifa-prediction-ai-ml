import kagglehub

# Download latest version of dataset
path = kagglehub.dataset_download("iamsouravbanerjee/fifa-football-world-cup-dataset")

print("Dataset downloaded to:", path)
