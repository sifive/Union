//////////////////////////////////////////////////////////// 
//  verilog module instance
//////////////////////////////////////////////////////////// 

`timescale 1ns/1ps


module childmod(input clk);


  int bigclk=0;

  initial  
  begin
    $display("hello world from verilog %m");
  end

  always@(clk)
    begin
      $display("hello world from verilog %m %h",clk);
      bigclk = bigclk+1;
    end

  testbench(bigclk[3]);

endmodule

module testbench(clk);
  input clk;

  always @(clk)
  begin
    $display("new clk edge verilog %m %h",clk);

  end

  //alternate_module(clk,req, ack, commit);
  real_sage_rtl(clk,req, ack, commit);
  dut(clk,req, ack, commit);

  initial 
    forever begin
    #1
      $display("values in %m req:%x ack:%x commit:%x",req,ack,commit);
    end

endmodule



module dut(clk , req, ack, commit);
  input clk;
  input req;
  output reg ack;
  input commit;

  assign ack = req;
endmodule



module alternate_module(clk,req, ack, commit);
  input clk;
  output reg req=0;
  input ack;
  output reg commit;


//  always @(clk)
//  begin
  initial
    force commit = ack;
//  end

  initial #10 req=1;

endmodule



module real_sage_rtl(clk,req, ack, commit);
  input clk;
  output reg req=0;
  input ack;
  output reg commit;

  assign commit = ack;

  initial #10 req=1;

endmodule


