import encoder
import planner
import decoder
import sys

orig_stdout = sys.stdout
f = open('mdpfile.txt', 'w')
sys.stdout = f
encoder.encoder_function('p2_policy2.txt', 'states_file_p1.txt')
f.close()

f = open('val_pol.txt', 'w')
sys.stdout = f
planner.planner_function('mdpfile.txt')
f.close()

f = open('policyfile1.txt', 'w')
sys.stdout = f
decoder.decoder_function('val_pol.txt', 'states_file_p1.txt', '1') 
f.close()


for i in range(15):
    f = open('mdpfile.txt', 'w')
    sys.stdout = f
    encoder.encoder_function('policyfile1.txt', 'states_file_p2.txt')
    f.close()
    
    f = open('val_pol.txt', 'w')
    sys.stdout = f
    planner.planner_function('mdpfile.txt')
    f.close()
    
    f = open('policyfile2.txt', 'w')
    sys.stdout = f
    decoder.decoder_function('val_pol.txt', 'states_file_p2.txt', '2')
    f.close()

    f = open('mdpfile.txt', 'w')
    sys.stdout = f
    encoder.encoder_function('policyfile2.txt', 'states_file_p1.txt')
    f.close()
    
    f = open('val_pol.txt', 'w')
    sys.stdout = f
    planner.planner_function('mdpfile.txt')
    f.close()
    
    f = open('policyfile1.txt', 'w')
    sys.stdout = f
    decoder.decoder_function('val_pol.txt', 'states_file_p1.txt', '1') 
    f.close()

f = open('mdpfile.txt', 'w')
sys.stdout = f
encoder.encoder_function('policyfile1.txt', 'states_file_p2.txt')
f.close()

f = open('val_pol.txt', 'w')
sys.stdout = f
planner.planner_function('mdpfile.txt')
f.close()

f = open('policyfile2.txt', 'w')
sys.stdout = f
decoder.decoder_function('val_pol.txt', 'states_file_p2.txt', '2')
f.close()

sys.stdout = orig_stdout
