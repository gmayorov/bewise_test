import os
import subprocess
import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


# Конвертирует .wav в .mp3 с использованием временного файла, возвращает True в случае успеха
def convert_to_mp3(file, path, filename: str) -> bool:
    temp_filename = generate_uuid() + '.tmp'
    file.save(temp_filename)
    mp3_full_path = os.path.join(path, filename)
    result_code = subprocess.call(f'lame {temp_filename} {mp3_full_path}', shell=True)
    os.remove(temp_filename)
    return not result_code
