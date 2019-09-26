
# tqdm

### What it is good for?

Drawing progress bars

### Installed with Python by default

no

### How to install it?

    pip install tqdm

### Example


    import time
    from tqdm import tqdm

    for i in tqdm(range(100)):
        time.sleep(0.1)

    66%|███████████████████████████▋              | 66/100 [00:06<00:03,  9.91it/s]
