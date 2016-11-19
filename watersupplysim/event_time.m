
%% Exponential distibuted event waiting time generation function
% Calculates de event with a exponential distribution. That is used
% to determine time between events.
function [time] = event_time(lambda)
   
    if lambda <= 0
        error('Lamnda must be a greater or equal to zero')
    end
    a = rand();
    time = (log(lambda) - log(a)) / lambda;
end
