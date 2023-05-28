import argparse

def f(x, y, z):
    return x, y, z

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=1)
    parser.add_argument("--y", type=int, default=2)
    parser.add_argument("--z", type=int, default=3)
    args = parser.parse_args()
    print(f(args.x, args.y, args.z))