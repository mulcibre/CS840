require "Win32API"

QueryPerformanceCounter = Win32API.new("kernel32",
                                       "QueryPerformanceCounter", 'P', 'I')
QueryPerformanceFrequency = Win32API.new("kernel32",
                                         "QueryPerformanceFrequency", 'P', 'I')

def get_ticks
  tick = ' ' * 8
  get_ticks = QueryPerformanceCounter.call(tick)
  tick.unpack('q')[0]
end

def get_freq
  freq = ' ' * 8
  get_freq =  QueryPerformanceFrequency.call(freq)
  freq.unpack('q')[0]
end

def get_time_diff(a, b)
  # This function takes two QPC ticks
  (b - a).abs.to_f / (get_freq)
end

numTimes = 10000
times = Array.new(numTimes)

(0...(numTimes)).each do |i|
  times[i] = get_ticks
end

durations = []
(0...(numTimes - 1)).each do |i|
  durations[i] = get_time_diff(times[i+1], times[i])
end

durations.each do |duration|
    p (duration * 1000000000).to_s + ','
end

p durations.inject{ |sum, el| sum + el }.to_f