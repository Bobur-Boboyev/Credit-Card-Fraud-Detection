import os
import shutil
import kagglehub

dataset_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")
source_file = os.path.join(dataset_path, "creditcard.csv")
target_dir = os.path.join(os.getcwd(), "data")
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "creditcard.csv")
shutil.copy(source_file, target_file)
