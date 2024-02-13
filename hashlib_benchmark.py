import hashlib
import time


def gen_random_file_cmd(of: str, bs: str, count: str) -> str:
    return 'dd if=/dev/urandom of=' + of + ' bs=' + bs + ' count=' + count


def read_file(file_name: str) -> bytes:
    with open(file_name, 'rb') as file_:
        return file_.read()


def sha512_bytes(bytes_: bytes) -> bytes:
    sha512 = hashlib.sha512()
    sha512.update(bytes_)
    return sha512.digest()


def sha512_iteration_bytes(bytes_: bytes, iterations: int) -> bytes:
    for _ in range(iterations):
        bytes_ = sha512_bytes(bytes_)

    return bytes_


if __name__ == '__main__':
    file_name = 'test'
    bs = 1024
    count = 512
    size_ = bs * count
    iterations = 1000000
    file_sha512_validate = b"\xec\xbd\xc0\r\xba\xee!\xe2y\xd3~\xa3\xd1R\x9f|\xa3\x7f\x97\xc8\xb8Vew\xd0K\xe3a\xcfT^\xf85\x92\xf6PTH\xb1\xd3\xde\x7f\x0c\xf1\xa13\xd8h\xee\xcf\x9eJ\xc99\x8du@\x92\x9c\xd4O\x98'\xad"

    print(gen_random_file_cmd(file_name, str(bs), str(count)))

    file_data = read_file(file_name)

    if len(file_data) != size_:
        raise Exception()

    start_time = time.time()
    file_sha512 = sha512_iteration_bytes(file_data, iterations)
    time_ = time.time() - start_time

    if file_sha512 != file_sha512_validate:
        raise Exception(file_sha512)

    print(iterations / time_)
