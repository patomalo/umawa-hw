%% Damped system
% evaluates damped systems solution
function y = damped_out(time , in, y_0, damp_factor)
    y = in*(1-exp(-damp_factor*in*time)) + y_0* exp(-damp_factor*time);
end