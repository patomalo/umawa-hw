%% Calculates samples from a unsampled time vector
% time vector is the time vector unsampled eg = [1, 5 ,5.61]
% We want to produce a vector of samples [1.0, 1.1, ... to .. 5.6] with
% residual time of 0.01 for next generation
% and the consumers signals within the sequence .._residual_on_off_....

function [out, time, residual] = samples_gen(time_vector, sample_period, initial_condition, damp_factor)
    N = floor(time_vector(end)/sample_period); % number of samples
    residual = time_vector(end) - N* sample_period;
    time = zeros(1,N);
    out = zeros(1,N);
    out(1) = damped_out(time(1), 0 , initial_condition, damp_factor);
    for i = 2:N
        time(i) =  (i-1) * sample_period;
        disp(time(i))
        
        if  time(i) > time_vector(1) && flag_residual ==1
            flag_residual = 0;
            initial_condition = out(i-1);
            disp 'change1'.
        elseif (time(i) > time_vector(1)) && (time(i) <= time_vector(2))
            disp 'g that residual but less than '
            out(i) = damped_out(time(i),1,initial_condition,damp_factor);
        else
            disp 'greater than all'
            out(i) = damped_out(time(i),0,initial_condition,damp_factor);
        end
        
        
        if  time_vector(1) >= time(i)
            disp 'less that residual'
            out(i) = damped_out(time(i),0,initial_condition,damp_factor);
            
        elseif (time(i) > time_vector(1)) && (time(i) <= time_vector(2))
            disp 'g that residual but less than '
            out(i) = damped_out(time(i),1,initial_condition,damp_factor);
        else
            disp 'greater than all'
            out(i) = damped_out(time(i),0,initial_condition,damp_factor);
        end
        
    end
end