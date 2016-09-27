/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Anuj Shah
 */
public class generateSeries extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
            /* TODO output your page here. You may use following sample code. */
            String totalNumbers = request.getParameter("totalNumbers");
            
            try {
                int first = 0;
                int second = 1;
                int total = Integer.parseInt(totalNumbers);
                if(total > 2 && total < 51) {
                    ArrayList FibonacciSeries = new ArrayList();
                    FibonacciSeries.add(first);
                    FibonacciSeries.add(second);

                    for(int i = 0 ; i < total - 2 ; i++ ){
                        int sum = first + second;
                        FibonacciSeries.add(sum);
                        first = second;
                        second = sum;
                    }
                    for(int i = 0 ; i < FibonacciSeries.size() ; i++){
                        out.println(FibonacciSeries.get(i) + "<br/>");

                    }
                } else {
                    out.print("Please enter number between 2 and 50 .<br/>");
                }
                out.print("<button onclick='window.location = \"index.html\"'>Go Back</button>");
                
            } catch(NumberFormatException ne){
                out.print("Please enter valid number");
                out.print("<button onclick='window.location = \"index.html\"'>Go Back</button>");
            }
        
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
