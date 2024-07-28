import json
from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

import poetry_version

__version__ = poetry_version.extract(source_file=__file__)


def run_turing_machine(
    machine: Dict,
    input_: str,
    steps: Optional[int] = None,
) -> Tuple[str, List, bool]:
    #pass  # Implement the function

    i = 10;
    i_min = 10;
    i_real = 10
    history=[]
    next_state = machine["start state"]
    actual_state = next_state
    my_input = machine["blank"] * 10 + input_
    step = 0
    while (next_state not in machine["final states"]) and (steps is None or step < steps):
        if i > len(my_input)-1:
            my_input = my_input + str(machine["blank"])
        actual_state = machine["table"][next_state][my_input[i]]


        curr = {
            "state": next_state,
            "reading": my_input[i],
            #"position": i-1000 if i-1000 >= 0 else 0,
            "position": i_real,
            "memory": my_input[i_min:].strip(machine["blank"]),
            "transition": {
            }
        }
        if "write" in actual_state:
            my_input = my_input[0:i] + actual_state["write"] + my_input[i+1:]
            curr["transition"]["write"]=actual_state["write"]
        side = ""
        if "R" in actual_state:
            i+=1
            if i_real <= len(input_)-1:
                i_real+=1
            side = "R"

        elif "L" in actual_state:
            if i_real > 0:
                i_real -=1
            i-=1
            side = "L"
        if isinstance(actual_state, dict):
            curr["transition"][side]=actual_state[side]
            next_state=actual_state[side]
        else:
            curr["transition"]=actual_state
        history.append(curr)
        #print (curr)
        if i < i_min:
            i_min=i
        step += 1

    halted = actual_state in machine["final states"]
    print("INPUT:")
    print(input_)
    print("MY_OUTPUT:")
    print("["+my_input.strip(machine["blank"])+"]")
    #return (my_input[i_min:].strip(machine["blank"]), history, halted)
    return (my_input.strip(machine["blank"]), history, halted)
