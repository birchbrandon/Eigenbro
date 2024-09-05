import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt


class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(True),
            nn.Linear(128, 64),
            nn.ReLU(True),
            nn.Linear(64, 12),
            nn.ReLU(True),
            nn.Linear(12, 3),  # Latent space representation
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(3, 12),
            nn.ReLU(True),
            nn.Linear(12, 64),
            nn.ReLU(True),
            nn.Linear(64, 128),
            nn.ReLU(True),
            nn.Linear(128, 784),
            nn.Tanh(),
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x


def main():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    criterion = nn.MSELoss()
    autoencoder = Autoencoder()
    optimizer = optim.Adam(autoencoder.parameters(), lr=0.001)

    num_epochs = 20

    for epoch in range(num_epochs):
        for data in train_loader:
            inputs, _ = data  # We don't need the labels, so we discard them
            inputs = inputs.view(inputs.size(0), -1)  # Flatten the images

            outputs = autoencoder(inputs)
            loss = criterion(outputs, inputs)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

    def imshow(img, title):
        img = img / 2 + 0.5  # unnormalize
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.show()

    dataiter = iter(train_loader)
    images, _ = next(dataiter)

    # Get a sample input
    sample = images[0].view(1, -1)

    # Get the reconstructed image
    with torch.no_grad():
        reconstructed = autoencoder(sample).view(28, 28)

    # Show original and reconstructed images
    imshow(images[0].view(28, 28), 'Original Image')
    imshow(reconstructed, 'Reconstructed Image')

    torch.save(autoencoder.state_dict(), "Autoendcoder/mnist_autoencoder.pth")


if __name__ == "__main__":
    main()
