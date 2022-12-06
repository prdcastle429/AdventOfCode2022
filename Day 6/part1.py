markerLength = 4
buffers = []
firstMarkerIndex = 0

with open("input.txt") as file:
    buffer = file.readline()
    for i in range(0, len(buffer)):
        if i < len(buffer) - (markerLength + 1):
            currBuffer = buffer[i:i+markerLength]
            buffers.append(currBuffer)

    for buffer in buffers:
        trimmedBuffer = [char for char in buffer if buffer.count(char) == 1]
        firstMarkerIndex += 1
        if len(trimmedBuffer) == markerLength:
            firstMarkerIndex += (markerLength - 1)
            break

print(firstMarkerIndex)