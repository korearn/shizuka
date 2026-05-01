from config import Config

def main():
    print(f'Starting system with DB at: {Config.DB_URL}')

if __name__ == '__main__':
    main()
