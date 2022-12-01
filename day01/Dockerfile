FROM python:3.10
COPY solution.py ./ input.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy
CMD python3 ./solution.py