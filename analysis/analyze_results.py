""" Analyze CAL training results """

import argparse
import pickle
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="Analyze a trusted CAL training log")
    parser.add_argument("log_path", help="Path to logged_record.pkl")
    args = parser.parse_args()
    with open(args.log_path, "rb") as f:
        data = pickle.load(f)

    keys = ["train/avg_acc", "test/avg_acc", "train/avg_loss", "test/avg_loss"]
    for key in keys:
        if key not in data:
            raise KeyError(f"Missing expected field: {key}")
    df = pd.DataFrame({
        "Epoch": range(len(data["train/avg_acc"])),
        "Train Accuracy": data["train/avg_acc"],
        "Test Accuracy": data["test/avg_acc"],
        "Train Loss": data["train/avg_loss"],
        "Test Loss": data["test/avg_loss"],
    })
    if "train/lr" in data:
        df["Learning Rate"] = data["train/lr"]
    if "train/alpha" in data:
        df["Alpha"] = data["train/alpha"]

    print(df.to_string(index=False))
    best_idx = df["Test Accuracy"].idxmax()
    print(f"\nBest test accuracy: {df.loc[best_idx, 'Test Accuracy']:.4f} (epoch index {df.loc[best_idx, 'Epoch']})")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(df["Epoch"], df["Train Accuracy"], label="Train")
    axes[0].plot(df["Epoch"], df["Test Accuracy"], label="Test")
    axes[0].set_title("Accuracy over epochs")
    axes[0].legend()
    axes[1].plot(df["Epoch"], df["Train Loss"], label="Train")
    axes[1].plot(df["Epoch"], df["Test Loss"], label="Test")
    axes[1].set_title("Loss over epochs")
    axes[1].legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
