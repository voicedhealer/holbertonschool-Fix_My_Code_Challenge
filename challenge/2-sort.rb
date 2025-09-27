#!/usr/bin/env ruby

# Filtrer uniquement les arguments qui sont des représentations numériques
numbers = ARGV.select { |x| x.match?(/^[-+]?\d+$/) }.map(&:to_i)
numbers.sort.each { |n| puts n }
