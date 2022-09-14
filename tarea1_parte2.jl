function is_pent_diag(M)
    for (i, row) in enumerate(eachrow(M))
        for (j, col) in enumerate(eachindex(row))
            if(abs(i-j) > 2)
                if(M[i,j] != 0)
                    return false
                end
            end
        end
    end
    return true
end

function det_penta(M)
    if(is_pent_diag(M))
        Pi_4 = M[1,1] #P1 = Pi_4
        Pi_3 = M[2,2]*Pi_4 - M[2,1]*M[1,2] # P2 = Pi_3
        Ri_3 = M[1,2] #R2 = Ri_3 
        Si_3 = M[2,1] #S2 = Si_3
        Pi_2 = M[3,3]*Pi_3 - M[3,2]*M[2,3]*Pi_4 - M[3,1]*M[1,3]*M[2,2] + M[3,1]*M[2,3]*Ri_3 + M[3,2]*M[1,3]*Si_3 #P3 = Pi_2
        Ri_2 = M[2,3]*Pi_4 - M[1,3]*Si_3 #R3 = Ri_2
        Si_2 = M[3,2]*Pi_4 - M[3,1]*Ri_3 #S3 = Si_2
        Pi_1 = M[4,4]*Pi_2 - M[4,3]*M[3,4]*Pi_3 - M[4,2]*M[2,4]*(M[3,3]*Pi_4 - M[3,1]*M[1,3]) + M[4,2]*M[3,4]*Ri_2 + M[4,3]*M[2,4]*Si_2 #P4 = Pi_1
        n = size(M,1)
        Pi = 0
        for i = 5:n
            Ri_1 = M[i-2,i-1]*Pi_3 - M[i-3,i-1]*Si_2
            Si_1 = M[i-1,i-2]*Pi_3 - M[i-1,i-3]*Ri_2
            Pi = M[i,i]*Pi_1 - M[i,i-1]*M[i-1,i]*Pi_2 - 
            M[i,i-2]*M[i-2,i]*(M[i-1,i-1]*Pi_3 - M[i-1,i-3]*M[i-3,i-1]*Pi_4) +
            M[i,i-2]*M[i-1,i]*Ri_1 + M[i,i-1]*M[i-2,i]*Si_1

            Pi_4 = Pi_3
            Pi_3 = Pi_2
            Pi_2 = Pi_1
            Pi_1 = Pi

            Ri_3 = Ri_2
            Ri_2 = Ri_1
            
            Si_3 = Si_2
            Si_2 = Si_1
        end
        return Pi
    else
        print("is not a pentadiagonal")
        return 0
    end
end

mat = [
        [1 2 3 0 0 0];
        [4 5 6 7 0 0];
        [8 9 10 11 12 0];
        [0 12 11 10 9 8];
        [0 0 7 6 5 4];
        [0 0 0 3 2 1];
        ]

println(det_penta(mat))