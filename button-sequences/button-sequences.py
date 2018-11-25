#!/usr/bin/env python
# -*- coding: utf-8 -*-

class State(object):
    def __init__(self):
        pass

    def on_event(self, event_red, event_blue):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

class NeitherState(State):
    def on_event(self, event_red, event_blue):
        if event_red=='1' and event_blue=='1':
            return RedState()
        elif event_red=='1' and event_blue=='0':
            return RedState()
        elif event_red=='0' and event_blue=='1':
            return BlueState()
        else:
            return self

class RedState(State):
    def on_event(self, event_red, event_blue):
        if event_red=='1' and event_blue=='1':
            return self
        elif event_red=='1' and event_blue=='0':
            return self
        elif event_red=='0' and event_blue=='1':
            return BlueState()
        else:
            return NeitherState()

class BlueState(State):
    def on_event(self, event_red, event_blue):
        if event_red=='1' and event_blue=='1':
            return self
        elif event_red=='1' and event_blue=='0':
            return RedState()
        elif event_red=='0' and event_blue=='1':
            return self
        else:
            return NeitherState()

class Sequencer(object):
    def __init__(self):
        self.state = NeitherState()
        self.result = ''

    def on_event(self, event_red, event_blue):
        if not self.state == self.state.on_event(event_red, event_blue):
            self.state = self.state.on_event(event_red, event_blue)
            if str(self.state) == 'RedState':
                self.result += 'R'
            elif str(self.state) == 'BlueState':
                self.result += 'B'

def button_sequences(seqR, seqB):
    seq = Sequencer()
    for i in range(0, len(seqR)):
        seq.on_event(seqR[i], seqB[i])
    return seq.result


print(button_sequences("10011010", "10110111"), "RBRB")
print(button_sequences("01001000", "01011100"), "RB")
print(button_sequences("01101000", "00111000"), "RB")
