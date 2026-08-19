class motormechanism:
    connection_made=False
    def make_electric_connection(self):
        self.connection_made=True
    def rotate(obj):
        if obj.connection_made:
            print("Start rotating")
        else:
            print("Please check connection => connection_made: ",obj.connection_made)
motor1=motormechanism()
motor1.make_electric_connection()
#motormechanism.rotate(motor1)
motor1.rotate()
