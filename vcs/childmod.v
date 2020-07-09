//////////////////////////////////////////////////////////// 
//  verilog module instance
//////////////////////////////////////////////////////////// 

`timescale 1ns/1ps


module childmod(input clk);


  int s;

  initial  
  begin
    $display("hello world from verilog %m");
    end

    always@(clk)
  begin
     
    $display("hello world from verilog %m %h",clk);
    end


endmodule
