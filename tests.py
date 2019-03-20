import pytest
import robot


class TestEdgeCasesLost(object):
    def test_edge_case_north_east(self):
        input = '5 3\n5 3 E\nF'
        assert robot.process_input(input) == ['5 3 E LOST']

    def test_edge_case_east_north(self):
        input = '5 3\n5 3 N\nF'
        assert robot.process_input(input) == ['5 3 N LOST']

    def test_edge_case_south_east(self):
        input = '5 3\n5 0 E\nF'
        assert robot.process_input(input) == ['5 0 E LOST']

    def test_edge_case_east_south(self):
        input = '5 3\n5 0 S\nF'
        assert robot.process_input(input) == ['5 0 S LOST']

    def test_edge_case_north_west(self):
        input = '5 3\n0 3 W\nF'
        assert robot.process_input(input) == ['0 3 W LOST']

    def test_edge_case_west_north(self):
        input = '5 3\n0 3 N\nF'
        assert robot.process_input(input) == ['0 3 N LOST']

    def test_edge_case_south_west(self):
        input = '5 3\n0 0 W\nF'
        assert robot.process_input(input) == ['0 0 W LOST']

    def test_edge_case_west_south(self):
        input = '5 3\n0 0 S\nF'
        assert robot.process_input(input) == ['0 0 S LOST']

    def test_edge_case_north(self):
        input = '5 3\n2 3 N\nF'
        assert robot.process_input(input) == ['2 3 N LOST']

    def test_edge_case_west(self):
        input = '5 3\n0 2 W\nF'
        assert robot.process_input(input) == ['0 2 W LOST']

    def test_edge_case_south(self):
        input = '5 3\n2 0 S\nF'
        assert robot.process_input(input) == ['2 0 S LOST']

    def test_edge_case_east(self):
        input = '5 3\n5 2 E\nF'
        assert robot.process_input(input) == ['5 2 E LOST']

class TestMovementOneDirection(object):
    def test_movement_east(self):
        for i in range(4):
            input = '5 3\n'+str(i)+' 0 E\nF'
            assert robot.process_input(input) == [str(i+1)+' 0 E']
    def test_movement_west(self):
        for i in reversed(range(1,4)):
            input = '5 3\n'+str(i)+' 0 W\nF'
            assert robot.process_input(input) == [str(i-1)+' 0 W']
    def test_movement_north(self):
        for i in range(3):
            input = '5 3\n0 '+str(i)+' N\nF'
            assert robot.process_input(input) == ['0 '+str(i+1)+' N']
    def test_movement_south(self):
        for i in reversed(range(1,3)):
            input = '5 3\n0 '+str(i)+' S\nF'
            assert robot.process_input(input) == ['0 '+str(i-1)+' S']

class TestMovementTwoDirections(object):
    def test_movement_north_east(self):
        for x in range(4):
            for y in range(3):
                input = '5 3\n'+str(x)+' '+str(y)+' E\nFLFR'
                assert robot.process_input(input) == [str(x+1)+' '+str(y+1)+' E']
    def test_movement_north_west(self):
        for x in reversed(range(1,4)):
            for y in range(1,3):
                input = '5 3\n'+str(x)+' '+str(y)+' W\nFRFL'
                assert robot.process_input(input) == [str(x-1)+' '+str(y+1)+' W']
    def test_movement_south_east(self):
        for x in range(1,4):
            for y in reversed(range(1,3)):
                input = '5 3\n'+str(x)+' '+str(y)+' E\nFRFL'
                assert robot.process_input(input) == [str(x+1)+' '+str(y-1)+' E']
    def test_movement_south_west(self):
        for x in reversed(range(1,4)):
            for y in reversed(range(1,3)):
                input = '5 3\n'+str(x)+' '+str(y)+' W\nFLFR'
                assert robot.process_input(input) == [str(x-1)+' '+str(y-1)+' W']
