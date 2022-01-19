import os

DEVICE_PATH = '/dev'


def main():
    print('Ready.')
    before = set(os.listdir(DEVICE_PATH))

    print('Now connect the device..')
    print('Connected? (yes/y) ', end='')
    input()

    after = set(os.listdir(DEVICE_PATH))

    new_device = after.difference(before)
    if new_device:
        print(f'\nTotal {len(new_device)} new Device(s) found:')
        for index, device in enumerate(list(new_device)):
            print(f'\t{index+1}.  {DEVICE_PATH}/{device}')
        print()
    else:
        print('\nNo new device found!')


if __name__ == '__main__':
    main()
