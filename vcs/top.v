// 

`timescale 1ns/1ps


module top();

  import "DPI-C" function void sample_dpi (input integer a);
  import "DPI-C" function void sample2 (input integer a);

  reg clk=0;
  int s;
  sc_top sc_top(.clk(clk));
  childmod childmod(.clk(clk));

  initial  
  begin
    $display("hello world from verilog %m");
    repeat(20)
  begin
    clk = !clk;
     #1 ;
    $display("hello world from verilog %m %h",clk);
    end
    sample_dpi(clk);
    sample2(clk);
    end


endmodule
