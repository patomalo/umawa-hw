events_number = 100 % this is the number of on events
e = zeros(2 * events_number); % the number of total events is the double
                              % since each on has its off
residual = 0; 
sample_period = 0.1 % sample period to apply a fourier transform
for i = 1:events_number
    e(i) = event_time(1);
end


plot(e)