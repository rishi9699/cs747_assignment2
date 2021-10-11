import encoder
import planner
import decoder
import sys

orig_stdout = sys.stdout
f = open('mdpfile.txt', 'w')
sys.stdout = f
encoder.encoder_function('data/attt/policies/p2_policy2.txt', 'data/attt/states/states_file_p1.txt')
f.close()

f = open('val_pol.txt', 'w')
sys.stdout = f
planner.planner_function('mdpfile.txt')
f.close()

f = open('policyfile1_0.txt', 'w')
sys.stdout = f
decoder.decoder_function('val_pol.txt', 'data/attt/states/states_file_p1.txt', '1') 
f.close()


for i in range(10):
    f = open('mdpfile.txt', 'w')
    sys.stdout = f
    encoder.encoder_function('policyfile1_' + str(i) + '.txt', 'data/attt/states/states_file_p2.txt')
    f.close()
    
    f = open('val_pol.txt', 'w')
    sys.stdout = f
    planner.planner_function('mdpfile.txt')
    f.close()
    
    f = open('policyfile2_' + str(i) + '.txt', 'w')
    sys.stdout = f
    decoder.decoder_function('val_pol.txt', 'data/attt/states/states_file_p2.txt', '2')
    f.close()

    f = open('mdpfile.txt', 'w')
    sys.stdout = f
    encoder.encoder_function('policyfile2_' + str(i) + '.txt', 'data/attt/states/states_file_p1.txt')
    f.close()
    
    f = open('val_pol.txt', 'w')
    sys.stdout = f
    planner.planner_function('mdpfile.txt')
    f.close()
    
    f = open('policyfile1_' + str(i+1) + '.txt', 'w')
    sys.stdout = f
    decoder.decoder_function('val_pol.txt', 'data/attt/states/states_file_p1.txt', '1') 
    f.close()

f = open('mdpfile.txt', 'w')
sys.stdout = f
encoder.encoder_function('policyfile1_10.txt', 'data/attt/states/states_file_p2.txt')
f.close()

f = open('val_pol.txt', 'w')
sys.stdout = f
planner.planner_function('mdpfile.txt')
f.close()

f = open('policyfile2_10.txt', 'w')
sys.stdout = f
decoder.decoder_function('val_pol.txt', 'data/attt/states/states_file_p2.txt', '2')
f.close()

sys.stdout = orig_stdout
