import qcdb

qcdb.set_molecule('db:S22-2-dimer')

# Default SS Scaling
E1 = qcdb.energy('mp2/6-31g*')
print(qcdb.print_variables())
qcdb.get_variable_details('SCS(N)-MP2 TOTAL ENERGY')

# Reset SS Scaling
qcdb.set_options({'mp2_ss_scale': 2,
                  'psi4_mp2_ss_scale': 30.0,
                 })

print(qcdb.get_active_options().print_changed())
E2 = qcdb.energy('mp2/6-31g*')
print(qcdb.print_variables())
qcdb.get_variable_details('SCS(N)-MP2 TOTAL ENERGY')

