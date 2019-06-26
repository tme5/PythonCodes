'''
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

Created on 25-Jun-2019

@author: Lenovo
'''
room_dict={}
time_slots=[(30, 75), (0, 50), (60, 150)]
for index,slot in enumerate(time_slots):
    if len(room_dict)==0:
        room_dict[f'room_{index}']=[slot]
    else:
        for room,booking in room_dict.items():
            for time_book in booking:
                if slot[0] in range(time_book[0],time_book[1]) or slot[1] in range(time_book[0],time_book[1]):
                    book_room=f'room_{index}'
                else:
                    book_room=room
                    
        if book_room not in room_dict.keys():
            room_dict[f'room_{index}']=[slot]
        else:
            room_dict[room].append(slot)

print(f'Number of rooms needed {str(len(room_dict))}')
print('----------')
print('Details:')
for room,slot in room_dict.items():
    print(f'    Room {room} has slot booking {slot}')
    