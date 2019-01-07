"""
A sample test writing out the error to the log and printing the failure message as the output.
"""
#START HERE
def test_my_output(): #1. Defining the method
 
      #2. Debug/progress messages
      import logging
      log = logging.getLogger('file_log') #A log handler
      fileHandler = logging.FileHandler('file_log.log')
      log.addHandler(fileHandler)
      streamHandler = logging.StreamHandler() #Write out to the command prompt
      log.addHandler(streamHandler)
 
      log.error('Hello from log: You should not see me in the pytest summary') #write into a log
      print 'Hello from print: You should not see me in the pytest summary' #
 
      #3. results summary section
      log.error('Hello from error: This is a summary of an error')
      print 'Hello from not-an-error: This is a summary of stdout aka not-an-error'
 
      #4. Example list of failures that your test may have collected
      test_metadata = 'firefox 45, OS X Yosemite'
      failure_list = ['1. Ineffective kiss. Frog did not turn into a prince.','2. The Queen used rat poison in the apple.','3. The birds   ate the breadcrumbs.']
      assert 3 == 3
 
#---START OF SCRIPT
if __name__=='__main__':
      #5. call the method
      test_my_output()
